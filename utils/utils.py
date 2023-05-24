
async def entry_to_database(table, data):
    table.insert(
        user_id=int(data.get('user_id')),
        weight=data.get('weight'),
        storage_time=data.get('storage_time'),
        phone=data.get('phone'),
        deliver=data.get('deliver'),
        address=data.get('address'),
        dimension=data.get('dimension'),
        cell_number='',
        expiration_time='',
        is_processed='n',
        date=data.get('date')
    )
    print('Данные записаны успешно в БД!')
    return
