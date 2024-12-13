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

def test_renderer_initialization(renderer):
    """Проверка инициализации рендерера."""
    assert renderer._width == 800
    assert renderer._height == 600

def test_renderer_add_game_object(renderer, game_object):
    """Проверка добавления игрового объекта."""
    renderer.add_game_object(game_object)
    assert game_object in renderer._game_objects

@patch('pygame.display.set_mode')
@patch('pygame.display.set_caption')
def test_renderer_setup(mock_set_caption, mock_set_mode):
    """Проверка инициализации экрана."""
    GameRenderer(800, 600)
    mock_set_mode.assert_called_once_with((800, 600))
    mock_set_caption.assert_called_once_with('Pacman')

@patch('pygame.font.SysFont')
def test_renderer_display_text(mock_font, renderer):
    """Проверка отображения текста."""
    mock_font.return_value.render.return_value = pygame.Surface((100, 50))
    renderer.display_text('Hello, World', (32, 32), 30)
    mock_font.assert_called_once_with('Arial', 30)

@patch('pygame.event.get')
def test_renderer_handle_events(mock_get_events, renderer):
    """Проверка обработки событий (выход из игры)."""
    mock_get_events.return_value = [pygame.event.Event(pygame.QUIT)]
    renderer._handle_events()
    assert renderer._done

@patch('pygame.draw.rect')
def test_renderer_draw_game_object(mock_draw_rect, renderer, game_object):
    """Проверка отрисовки объекта."""
    renderer.add_game_object(game_object)
    game_object.draw()
    mock_draw_rect.assert_called_once()
