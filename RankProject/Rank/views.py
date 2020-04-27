import uuid

from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from Rank.models import RankModels
from Rank.serializers import RankSerializers


class CreadeFractionView(CreateAPIView):
    queryset = RankModels.objects.all()
    serializer_class = RankSerializers

    def post(self, request, *args, **kwargs):
        client = request.data.get('client')
        fraction = int(request.data.get('fraction'))
        rank = RankModels.objects.filter(client=client)
        # 数据库中依据client查找数据，找到代表之前创建过，直接修改grade(排名)、fraction(分数)
        # 找不到则代表第一次创建，就创建并保存数据
        if rank:
            rank = rank[0]
            count = len(RankModels.objects.filter(fraction__gte=fraction))
            grade = count + 1
            rank.fraction = fraction
            rank.grade = grade
            rank.save()
        else:
            rank = RankModels()
            rank.client = client
            rank.fraction = fraction
            count = RankModels.objects.filter(fraction__gte=fraction)
            grade = len(count) + 1
            rank.grade = grade
            rank.save()
        # 缓存token值，在第二接口中使用token值取调用接口的client
        token = generate_token()
        cache.set(token, rank.id)

        data = {
            'status': 200,
            'msg': 'create success',
            'token': token,
            'rank': {
                'id': rank.id,
                'grade': rank.grade,
                'client': rank.client,
                'fraction': rank.fraction
            }
        }
        return Response(data)


class ListRankView(ListAPIView):
    queryset = RankModels.objects.all()
    serializer_class = RankSerializers

    def get(self, request, *args, **kwargs):
        # 定义查询排行起始、终止值，默认查整个排行榜
        count = len(RankModels.objects.all())
        start = request.query_params.get('start', 0)
        end = request.query_params.get('end', count)
        try:
            # 根据接口一的token获得调用本接口的client，并获取client信息
            token = request.query_params.get('token')
            rank_id = cache.get(token)
            rank = RankModels.objects.get(pk=rank_id)
        except Exception as e:
            raise ValidationError(detail="请提供token")
        # 排行榜信息
        rank_list = RankModels.objects.filter(grade__range=(start, end)).order_by('grade')

        data = {
            'msg': 'ok',
            'status': 200,
            # 排行榜信息，在下面for循环中添加数据
            'ranks': [],
            # 调用此接口者信息
            'rank': {
                'id': rank.id,
                'grade': rank.grade,
                'client': rank.client,
                'fraction': rank.fraction
            }
        }
        for rk in rank_list:
            data['ranks'].append({
                'id': rk.id,
                'grade': rk.grade,
                'client': rk.client,
                'fraction': rk.fraction
            })
        return Response(data)


# 生成token
def generate_token():
    token = uuid.uuid4().hex
    return token
