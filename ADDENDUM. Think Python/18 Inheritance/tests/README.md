Где то к середине сообразил, что не очень удачно все это организовал:

нужно было создать отдельный модуль с константами - наборами карт (с осмысленными названиями), а в каждом тестовом классе его просто импортировать и использовать в методах _test_deck_with_...()
вместо того, чтобы каждый раз задавать их в методе _setUp()_.

Но переделывать уже не буду - просто зафиксируем.

Кстати, уже в самом финале, именно когда писал тесты для метода _classify()_, обнаружил в нем ошибку (неправильно определялась комбинация "Straight flush" для несортированного набора карт). Так что тестирование рулит!