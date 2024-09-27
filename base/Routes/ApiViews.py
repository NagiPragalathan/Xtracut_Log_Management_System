from django.shortcuts import render, redirect
# from base.models import Contact_us
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from ..models import LogModel
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from urllib.parse import parse_qs

# Create your views here.

def Home(request):
    return render(request,"index.html")

# for SEO...

def robots_txt(request):
    content = "User-agent: *\nDisallow: /private/\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")


# API
@csrf_exempt
def api_create_log(request):
    if request.method == 'POST':
        try:
            # Debugging: Print the raw request body to confirm the format
            print(request.body.decode('utf-8'))

            # If the data is URL-encoded, parse it using urllib's parse_qs
            data = parse_qs(request.body.decode('utf-8'))

            # Extracting data from the parsed dictionary (values will be lists)
            log_msg = data.get('log_msg', [None])[0]
            status_code = data.get('StatusCode', [None])[0]
            user_mailid = data.get('user_mailid', [None])[0]
            plugin = data.get('Plugin', [None])[0]
            function = data.get('function', [None])[0]
            
        except Exception as e:
            # Handle any unexpected parsing errors
            print(f"Error occurred: {str(e)}")
            return JsonResponse({"error": "Invalid data format"}, status=400)

        # Validate missing fields
        if not all([log_msg, status_code, user_mailid, plugin, function]):
            return JsonResponse({"error": "Missing data fields"}, status=400)

        # Create the log entry
        log_entry = LogModel.objects.create(
            log_msg=log_msg,
            StatusCode=status_code,
            user_mailid=user_mailid,
            Plugin=plugin,
            function=function,
            dateTime=timezone.now()
        )

        return JsonResponse({"message": "Log entry created", "log_id": log_entry.userid}, status=201)

    return HttpResponse(status=405)  # Method not allowed


# Read a log entry
def api_read_log(request, log_id):
    log_entry = get_object_or_404(LogModel, userid=log_id)
    data = {
        'log_msg': log_entry.log_msg,
        'StatusCode': log_entry.StatusCode,
        'user_mailid': log_entry.user_mailid,
        'Plugin': log_entry.Plugin,
        'function': log_entry.function,
        'dateTime': log_entry.dateTime,
    }
    return JsonResponse(data)

# Update a log entry
@csrf_exempt
def api_update_log(request, log_id):
    log_entry = get_object_or_404(LogModel, userid=log_id)
    
    if request.method == 'POST':
        log_entry.log_msg = request.POST.get('log_msg', log_entry.log_msg)
        log_entry.StatusCode = request.POST.get('StatusCode', log_entry.StatusCode)
        log_entry.user_mailid = request.POST.get('user_mailid', log_entry.user_mailid)
        log_entry.Plugin = request.POST.get('Plugin', log_entry.Plugin)
        log_entry.function = request.POST.get('function', log_entry.function)
        log_entry.dateTime = timezone.now()
        
        log_entry.save()
        return JsonResponse({"message": "Log entry updated"})
    return HttpResponse(status=405)  # Method not allowed

# Delete a log entry
@csrf_exempt
def api_delete_log(request, log_id):
    log_entry = get_object_or_404(LogModel, userid=log_id)
    
    if request.method == 'DELETE':
        log_entry.delete()
        return JsonResponse({"message": "Log entry deleted"}, status=204)
    
    return HttpResponse(status=405)  # Method not allowed


def api_list_logs(request):
    logs = LogModel.objects.all()
    data = [
        {
            'log_msg': log.log_msg,
            'StatusCode': log.StatusCode,
            'user_mailid': log.user_mailid,
            'Plugin': log.Plugin,
            'function': log.function,
            'dateTime': log.dateTime,
        }
        for log in logs
    ]
    return JsonResponse(data, safe=False)