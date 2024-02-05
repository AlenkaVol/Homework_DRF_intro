from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# 1 Создать датчик. Указываются название и описание датчика.
# 4 Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 3 Добавить измерение. Указываются ID датчика и температура.
class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# 2 Изменить датчик. Указываются название и описание.
# 5 Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание
# и список всех измерений с температурой и временем.
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer