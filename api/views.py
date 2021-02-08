from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

# REST FRAMEWORK
from rest_framework import viewsets
from rest_framework import generics, mixins

# APPLICATION MODULES
from .serializers import *
from .models import *



# TOTAL_BANKS = Bank.objects.all().count()
# TOTAL_BRANCHES = Branch.objects.all().count()


def index(request):
	# print(TOTAL_BANKS, TOTAL_BRANCHES)
	return render(request,"index.html")

class BranchSearchView(mixins.ListModelMixin,generics.GenericAPIView):
	serializer_class = BranchSerializer

	def get_queryset(self,*args,**kwargs):

		user_query = self.request.query_params.get("q")
		limit = self.request.query_params.get("limit")
		offset = self.request.query_params.get("offset")
		
		offset = int(self.request.query_params.get("offset")) if offset else 0
		limit = int(self.request.query_params.get("limit")) if limit else 250

		limit += offset
	
		if user_query:
			queryset=Branch.objects.filter(Q(ifsc__icontains=user_query)|Q(bank_id__icontains=user_query)|Q(branch__icontains=user_query)|Q(address__icontains=user_query)|Q(city__icontains=user_query)|Q(district__icontains=user_query)|Q(state__icontains=user_query)).order_by('ifsc')
			queryset = queryset[offset:limit]
			return queryset

		else:
			queryset = Branch.objects.order_by("ifsc")[offset:limit]
			return queryset

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)



class BranchAutoCompleteSearchView(mixins.ListModelMixin,generics.GenericAPIView):
	serializer_class = BranchSerializer

	def get_queryset(self,*args,**kwargs):
		user_query = self.request.query_params.get("q")
		limit = self.request.query_params.get("limit")
		offset = self.request.query_params.get("offset")
		
		offset = int(self.request.query_params.get("offset")) if offset else 0
		limit = int(self.request.query_params.get("limit")) if limit else 250
		
		limit += offset
		# limit = TOTAL_BRANCHES if limit > TOTAL_BRANCHES else limit

		# offset = TOTAL_BRANCHES if offset > TOTAL_BRANCHES else offset

		if user_query:
			queryset=Branch.objects.filter(Q(branch__icontains=user_query)).order_by('ifsc')
			queryset = queryset[offset:limit]
			return queryset

		else:
			queryset = Branch.objects.order_by("ifsc")[offset:limit]
			return queryset

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)




def set_favourite(request,pk):
	branch = Branch.objects.get(ifsc=pk)

	branch.is_favourite = True
	branch.save()
	
	result = str(pk) + " favourite set to " + str(branch.is_favourite)
	return HttpResponse(result)

