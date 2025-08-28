from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'email', 'age']
    success_url = reverse_lazy('student_list')
    success_message = "Student created successfully!"

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['name', 'email', 'age']
    success_url = reverse_lazy('student_list')
    success_message = "Student updated successfully!"

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)
