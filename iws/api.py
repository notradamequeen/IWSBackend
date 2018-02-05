from iws.models import Field, RiskType, Form
from iws.serializers import FieldSerializer, RiskTypeSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class RiskTypeList(generics.ListCreateAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer

    def get_serializer(self,instance=None, data=None, many=False, partial=False):
        if self.request.method == 'POST':
            return super(RiskTypeList, self).get_serializer(instance=instance, data=data, many=True, partial=partial)
        return super(RiskTypeList, self).get_serializer()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = RiskTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer = RiskTypeSerializer(data=self.request.data, many=True)
        if serializer.is_valid():
            serializer.save()


class RiskTypeDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def get_serializer(self, instance=None, data=None, many=False, partial=False):
        if self.request.method == 'POST':
            return super(FieldList, self).get_serializer(instance=instance, data=data, many=True, partial=partial)
        return super(FieldList, self).get_serializer()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = FieldSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer = FieldSerializer(data=self.request.data, many=True)
        if serializer.is_valid():
            serializer.save()


class FieldDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FormAPIView(APIView):
    queryset = Form.objects.all()
    # serializer_class = FormSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        field = Field.objects.get(pk=int(data['field']))
        risk_type = RiskType.objects.get(pk=int(data['risk_type']))
        created_form = Form.objects.create(field=field, risk_type=risk_type)

        if(created_form):
            return Response({"success": "success"})
