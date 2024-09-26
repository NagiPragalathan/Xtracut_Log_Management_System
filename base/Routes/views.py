from django.shortcuts import render, get_object_or_404, redirect
from base.models import LogModel
from django.utils import timezone

# Create a log entry
def create_log(request):
    if request.method == 'POST':
        log_msg = request.POST.get('log_msg')
        status_code = request.POST.get('StatusCode')
        user_mailid = request.POST.get('user_mailid')
        plugin = request.POST.get('Plugin')
        function = request.POST.get('function')
        
        log_entry = LogModel.objects.create(
            log_msg=log_msg,
            StatusCode=status_code,
            user_mailid=user_mailid,
            Plugin=plugin,
            function=function,
            dateTime=timezone.now()
        )
        return redirect('log_list')  # Redirect to list of logs
    return render(request, 'admin/create_log.html')

# Read a log entry
def log_list(request):
    logs = LogModel.objects.all()
    return render(request, 'admin/log_list.html', {'logs': logs})

# Update a log entry
def update_log(request, log_id):
    log_entry = get_object_or_404(LogModel, userid=log_id)
    
    if request.method == 'POST':
        log_entry.log_msg = request.POST.get('log_msg', log_entry.log_msg)
        log_entry.StatusCode = request.POST.get('StatusCode', log_entry.StatusCode)
        log_entry.user_mailid = request.POST.get('user_mailid', log_entry.user_mailid)
        log_entry.Plugin = request.POST.get('Plugin', log_entry.Plugin)
        log_entry.function = request.POST.get('function', log_entry.function)
        log_entry.dateTime = timezone.now()
        
        log_entry.save()
        return redirect('log_list')
    return render(request, 'admin/update_log.html', {'log_entry': log_entry})

# Delete a log entry
def delete_log(request, log_id):
    log_entry = get_object_or_404(LogModel, userid=log_id)
    
    if request.method == 'POST':
        log_entry.delete()
        return redirect('log_list')
    return render(request, 'admin/delete_log.html', {'log_entry': log_entry})
 