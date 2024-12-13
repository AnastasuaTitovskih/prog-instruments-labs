import pytest
from unittest.mock import Mock, patch
import pygame
from main import GameRenderer, GameObject

@pytest.fixture
def mock_renderer():
    """Создает мок для рендера."""
    class MockRenderer:
        def __init__(self):
            self._screen = pygame.Surface((800, 600))
    return MockRenderer()

@pytest.fixture
def game_object(mock_renderer):
    """Создает объект GameObject."""
    return GameObject(mock_renderer, 50, 50, 32)

@pytest.fixture
def renderer():
    """Создает экземпляр GameRenderer."""
    return GameRenderer(800, 600)

def test_game_object_initialization(game_object):
    """Проверка инициализации объекта."""
    assert game_object.x == 50
    assert game_object.y == 50
    assert game_object._size == 32

def test_game_object_set_position(game_object):
    """Проверка установки позиции."""
    game_object.set_position(100, 100)
    assert game_object.x == 100
    assert game_object.y == 100

@patch('pygame.draw.circle')
def test_game_object_draw_circle(mock_draw_circle, game_object):
    """Проверка отрисовки круга."""
    game_object._circle = True
    game_object.draw()
    mock_draw_circle.assert_called_once()