def find_stations(states_needed, stations):
    final_stations = []

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states # возвращает пересечение множеств. Штаты которые нужны для покрытия и которые есть в покрытии у этой станции
            if len(covered) > len(states_covered): # если покрытие максимально
                best_station = station
                states_covered = covered
        states_needed -= states_covered # убираем штаты из покрытия, покрываемой найденной станцией
        final_stations.append(best_station) # добавляем станцию в результат

    return final_stations


if __name__ == '__main__':
    # найти минимальное количество станций с покрытием всех штатов
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "са", "az"])

    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "са"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    print(find_stations(states_needed, stations))
