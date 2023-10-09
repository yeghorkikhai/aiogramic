from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.cbdata import BotCallbackData


async def test(
        message: Message,
        state: FSMContext,
        callback_data: BotCallbackData
) -> None:
    pass