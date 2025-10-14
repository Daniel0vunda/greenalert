from django.shortcuts import render , redirect
from .forms import WasteReportForm
from .models import WasteReport

def submit_report(request):
    if request.method == 'POST':
        form = WasteReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report_success')
    else:
        form = WasteReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

def report_list(request):
    reports = WasteReport.objects.all().order_by('-date_submitted')
    return render(request, 'report_list.html', {'reports': reports})
# Create your views here.
def report_success(request):
    return render(request, 'reports/report_success.html')
