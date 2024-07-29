# Технологии и методы программирования

## Лабораторная 5 "Unit tests"
В рамках данной лабораторной работы требуется продемонстрировать свой талант к покрытию кода тестами.
## Задание на лабораторную работу
1. Создать отдельную ветку в своем [форке](https://docs.github.com/en/get-started/quickstart/fork-a-repo) данного репозитория.
2. Подобрать код проекта, который вы будете покрывать юнит-тестами. Он может быть как вашим собственным, так и опесорсным.
2. Покрыть код юнит-тестами, руководствуясь материалом [лекции](https://github.com/xtrueman/prog_instruments/blob/main/presentations/UnitTests.pptx).
4. Открыть [пул-риквест](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) в иcходный репозиторий
5. Удостовериться, что github action успешно обнаружил и запустил ваши юнит-тесты, после чего ожидать ревью.

## Условия сдачи
* Использовать разрешено только **[pytest](https://docs.pytest.org/en/7.4.x/)**.
* Минимальное количество тестов - **7** штук.
* Как минимум **2** теста должны быть менее примитивными, чем основная масса, и использовать помимо ассертов параметризованное тестирование, моки, стабы и т.д.

## Ремарки:
* Очевидно, что при реализации юнит-тестов вы должны стремиться покрыть как можно больший процент кода тестами.
* Выбирайте в качестве исходного кода что-то более сложное, чем одинокий модуль с двумя функциями, считающими сумму чисел.
* Помните о правилах [test discovery](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#conventions-for-python-test-discovery).

<details>
  <summary> Немного про github action в этом репозитории </summary>
  <br>

Этот action выполняет крайне простой набор действий:
* Чекаутит код вашего форка,
* Устанавливает зависимости из `requirements.txt`,
* Запускает юнит-тесты,
* Подсчитывает процент покрытия кода тестами.

Как выглядит исполнение action здорового человека:

**1. Все зависимости успешно поставились**  
![image](https://github.com/itsecd/ptm-5/assets/70561974/86ff1acd-d080-4a18-b6e1-2c50bfdf7b7e)

**2. Все юнит-тесты успешно обнаружились и отработали**
![image](https://github.com/itsecd/ptm-5/assets/70561974/97807c55-0fc9-4ecb-ba2d-ca2922e8e107)

Хотя в саммари отображается число всех запусков кода, параметризованный тест для сдачи лабы считается за один.  
![image](https://github.com/itsecd/ptm-5/assets/70561974/df86f7cd-4cc5-43ae-aca7-2e3355c4b0d0)

**3. Все файлы исходного кода проекта отобразились в отчете**  
![image](https://github.com/itsecd/ptm-5/assets/70561974/42961202-40c1-44f6-8223-2a9e1e66cbbf)

  <br>
</details>


Если вы столкнулись с непреодолимыми трудностями в ходе выполнения лабораторной работы, вы можете задать вопрос в:
* в виде [ишью](https://github.com/itsecd/prog_instruments_labs/issues/new/choose) в этом репозитории,
* в разделе [Q&A](https://github.com/itsecd/prog_instruments_labs/discussions/categories/q-a) дискуссий в этом репозитории,
* телеграм-чате предмета,
* телеграм-чате вашего курса,
* канале в дискорде.