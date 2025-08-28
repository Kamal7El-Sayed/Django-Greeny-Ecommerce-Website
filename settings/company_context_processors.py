from .models import Company


def git_info(request):
    info = Company.objects.last()

    return {"info": info}
