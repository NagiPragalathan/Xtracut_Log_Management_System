from django.shortcuts import render
from django.http import HttpResponse
from base.models import LogModel
from django.utils import timezone
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 

@login_required(login_url='/login/') 
def dashboard(request):
    logs = LogModel.objects.all()
    total_log = len(logs)
     # Get the selected filters from the form
    time_filter = request.GET.get('time_filter')
    plugin_filter = request.GET.get('plugin_filter')
    status_code_filter = request.GET.get('status_code_filter')
    function_filter = request.GET.get('function_filter')
    user_mailid_filter = request.GET.get('user_mailid_filter')

    # Get the current time
    now = timezone.now()

    success = logs.filter(StatusCode=201)
    error = logs.filter(StatusCode=500)
    
    # Apply time filter
    if time_filter == '30_minutes':
        logs = logs.filter(dateTime__gte=now - timedelta(minutes=30))
    elif time_filter == '1_hour':
        logs = logs.filter(dateTime__gte=now - timedelta(hours=1))
    elif time_filter == '1_week':
        logs = logs.filter(dateTime__gte=now - timedelta(weeks=1))
    elif time_filter == '1_month':
        logs = logs.filter(dateTime__gte=now - timedelta(days=30))

    # Apply plugin filter
    if plugin_filter and plugin_filter != 'all':
        logs = logs.filter(Plugin=plugin_filter)

    # Apply status code filter
    if status_code_filter and status_code_filter != 'all':
        logs = logs.filter(StatusCode=status_code_filter)

    # Apply function filter
    if function_filter and function_filter != 'all':
        logs = logs.filter(function=function_filter)

    # Apply user mail filter
    if user_mailid_filter:
        logs = logs.filter(user_mailid__icontains=user_mailid_filter)

    unique_emails = LogModel.objects.values_list('user_mailid', flat=True).distinct()
    unique_plugins = LogModel.objects.values_list('Plugin', flat=True).distinct()
    unique_status_codes = LogModel.objects.values_list('StatusCode', flat=True).distinct()
    unique_functions = LogModel.objects.values_list('function', flat=True).distinct()

    return render(request, 'dashboard.html',  {
        'logs': logs,
        'total_log': total_log,
        'time_filter': time_filter,
        'plugin_filter': plugin_filter,
        'status_code_filter': status_code_filter,
        'function_filter': function_filter,
        'user_mailid_filter': user_mailid_filter,
        'unique_emails': unique_emails,
        "success":len(success),
        "error":len(error),
        "unique_plugins":len(unique_plugins),
        "unique_status_codes":len(unique_status_codes),
        "unique_functions": unique_functions
    })

def filter(request):
    return render(request, 'filter.html')


def get_chart_data(request):
    today = timezone.now().date()
    last_7_days = [(today - datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    
    success_logs = []
    error_logs = []
    
    # Assuming we want to differentiate based on the Plugin field as well
    plugin_filter = request.GET.get('plugin', '')  # Get plugin filter from query params if available

    for day in last_7_days:
        start_date = datetime.datetime.strptime(day, '%Y-%m-%d').date()
        end_date = start_date + datetime.timedelta(days=1)

        # Query logs for each StatusCode and Plugin
        if plugin_filter:
            success_count = LogModel.objects.filter(StatusCode='201', Plugin=plugin_filter, dateTime__range=[start_date, end_date]).count()
            error_count = LogModel.objects.filter(StatusCode='500', Plugin=plugin_filter, dateTime__range=[start_date, end_date]).count()
        else:
            success_count = LogModel.objects.filter(StatusCode='201', dateTime__range=[start_date, end_date]).count()
            error_count = LogModel.objects.filter(StatusCode='500', dateTime__range=[start_date, end_date]).count()

        # Append the counts to respective lists
        success_logs.append(success_count)
        error_logs.append(error_count)

    # Return JSON response with labels (dates) and datasets
    return JsonResponse({
        'labels': last_7_days,
        'datasets': {
            'success': success_logs,
            'error': error_logs,
        }
    })