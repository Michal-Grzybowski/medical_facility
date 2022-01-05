from datetime import datetime
from typing import Dict, List, Optional, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.common import add_entity, delete_entity, get_entities, get_entity, update_entity
from app.models.doctor import Doctor


async def get_doctors(session: AsyncSession):
    return await get_entities(session, Doctor)


# async def get_doctors_by_specialty(specialty: str):
#     doctors = [
#         doctor async for doctor in doctor_collection.find(
#             {"specialties":specialty})
#     ]
#     return doctors


async def get_doctor(session: AsyncSession, doctor_id: str):
    return await get_entity(session, Doctor, doctor_id)


async def add_doctor(session: AsyncSession, doctor_data: dict):
    return await add_entity(session, Doctor, doctor_data)


async def update_doctor(session: AsyncSession, doctor_id: str, doctor_data: dict):
    return await update_entity(session, Doctor, doctor_data, doctor_id)


# async def update_doctor_schedule(
#         doctor_id: str, new_schedule: Dict[Tuple[datetime, datetime],
#                                            List[Tuple[datetime, datetime,
#                                                       Optional[str]]]]):
#     doctor = await get_doctor(doctor_id)
#     doctor.schedule.append(new_schedule)
#     return update_doctor(doctor_id, doctor.dict())


# async def add_appointment(
#         doctor_id: str, appointment: Tuple[datetime, datetime]):
#     doctor = await get_doctor(doctor_id)
#     doctor.scheduled_appointments.append(appointment)
#     return update_doctor(doctor_id, doctor.dict())


# async def update_appointment(
#         doctor_id: str, appointment: Tuple[datetime, datetime], description: str):
#     doctor = await get_doctor(doctor_id)
#     doctor.scheduled_appointments.remove(appointment)
#     doctor.scheduled_appointments.append((appointment[0], appointment[1], description))
#     return update_doctor(doctor_id, doctor.dict())


# async def update_doctor_specialty(doctor_id: str, new_specialty: dict):
#     doctor = await get_doctor(doctor_id)
#     doctor.specialties.append(new_specialty)
#     return update_doctor(doctor_id, doctor.dict())


async def delete_doctor(session: AsyncSession, doctor_id: str):
    return await delete_entity(session, Doctor, doctor_id)
