from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 모델이 추가될때만 갱신
    updated = models.DateTimeField(auto_now=True)  # 매번 갱신

    # 해당 모델이 데이터베이스로 가기를 원하지 않음
    class Meta:
        abstract = True  # 데이터베이스에 나타나지 않은 모델
