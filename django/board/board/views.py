from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

from django.core.paginator import Paginator


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()

        return render(request, "board/question_form.html", {"form": form})


def answer_create(request, qid):
    """답변등록"""
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:question_detail", qid=qid)
    else:
        form = AnswerForm()

    # 방법1
    # answer = Answer.objects.create(
    #     question=question, content=request.POST.get("content")
    # )

    # 방법2
    # question.answer_set.create(content = request.POST.get("content"))

    # 방법3
    # answer = Answer(question = question, content = request.POST.get("content"))
    # answer.save()

    # 실패 시 get 방식으로 처리
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


def question_list(request):
    """전체 질문 추출"""

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)

    # question_list = Question.objects.all()
    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}
    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {"question": question}
    return render(request, "board/question_detail.html", context)