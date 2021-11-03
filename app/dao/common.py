from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection


async def get_entities(collection: AsyncIOMotorCollection):
    entities = [entity async for entity in collection.find()]
    return entities


async def get_entity(collection: AsyncIOMotorCollection, entity_id: str):
    entity = await collection.find_one({'_id': ObjectId(entity_id)})
    if entity:
        return entity


async def add_entity(collection: AsyncIOMotorCollection, entity_data: dict):
    entity = await collection.insert_one(entity_data)

    return entity


async def update_entity(collection: AsyncIOMotorCollection, entity_data: dict, entity_id: str):
    """Function returns False if request body is empty or entity with given id doesn't exist"""
    if len(entity_data) < 1:
        return None
    entity = await collection.find_one({"_id": ObjectId(entity_id)})
    if entity:
        updated_entity = await collection.update_one({"_id": ObjectId(entity_id)}, {"$set": entity_data})

        if updated_entity:
            return updated_entity
    return None


async def delete_entity(collection: AsyncIOMotorCollection, entity_id: str):
    """Function returns False if entity with given id doesn't exist"""
    entity = await collection.find_one({"_id": ObjectId(entity_id)})
    if entity:
        await collection.delete_one({"_id": ObjectId(entity_id)})
        return True
    return False