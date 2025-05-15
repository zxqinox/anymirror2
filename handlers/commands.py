from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🤖 Добро пожаловать в Bot Factory!\n"
        "Используйте /create_template для создания нового шаблона"
    )

@router.message(Command("create_template"))
async def create_template(message: Message, state: FSMContext):
    await state.set_state("template_name")
    await message.answer("Введите название для нового шаблона:")
