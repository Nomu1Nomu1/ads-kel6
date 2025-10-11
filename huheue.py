from typing import List, Dict

# data
mhs = [
    {"nama": "Ayu Lestari", "nim": "V2301001", "kelas": "TI-A", "nilai": 88},
    {"nama": "Budi Santoso", "nim": "V2301002", "kelas": "TI-A", "nilai": 74},
    {"nama": "Citra Dewi", "nim": "V2301003", "kelas": "TI-A", "nilai": 91},
    {"nama": "Doni Pratama", "nim": "V2301004", "kelas": "TI-B", "nilai": 65},
    {"nama": "Eka Putra", "nim": "V2301005", "kelas": "TI-B", "nilai": 70},
    {"nama": "Farah Azizah", "nim": "V2301006", "kelas": "TI-A", "nilai": 95},
    {"nama": "Gilang Ramadhan", "nim": "V2301007", "kelas": "TI-C", "nilai": 85},
    {"nama": "Hani Kusuma", "nim": "V2301008", "kelas": "TI-C", "nilai": 92},
    {"nama": "Indra Wijaya", "nim": "V2301009", "kelas": "TI-B", "nilai": 80},
    {"nama": "Joko Saputra", "nim": "V2301010", "kelas": "TI-C", "nilai": 78},
    {"nama": "Kiki Amalia", "nim": "V2301011", "kelas": "TI-A", "nilai": 82},
    {"nama": "Lina Marlina", "nim": "V2301012", "kelas": "TI-C", "nilai": 68},
    {"nama": "Miko Ananda", "nim": "V2301013", "kelas": "TI-B", "nilai": 89},
    {"nama": "Nina Safitri", "nim": "V2301014", "kelas": "TI-B", "nilai": 94},
    {"nama": "Oka Darmawan", "nim": "V2301015", "kelas": "TI-C", "nilai": 76},
]

# Sort
def insertion(data: List[Dict], key: str, reverse = False) -> List[Dict]:
    arr = data.copy()
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j][key] > current[key] ^ reverse)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

def merge_srt(data: List[Dict], key: str, reverse = False) -> List[Dict]:
    if len(data) < 1:
        return data
    mid = len(data) // 2
    left = merge_srt(data[:mid], key, reverse)
    right = merge_srt(data[mid:], key, reverse)
    return merge_srt(left, right, key, reverse)

def merge(left, right, key, reverse):
    result = []
    while left and right:
        if (left[0][key] <= right[0][key]) ^ reverse:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left if left else right)
    return result

# Algotihm
def binary(data: List[Dict], target, key: str):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid][key] == right:
            return data[mid]
        elif data[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

# utility
def show_data(data: List[Dict]):
    print("\n{:<4} {:<20} {:<10} {:<8} {:<6}".format("No", "Nama", "NIM", "Kelas", "Nilai"))
    print("=" * 55)
    for i, mhs in enumerate(data, 1):
        print(f"{i:<4} {mhs['nama']:<20} {mhs['nim']:<10} {mhs['kelas']:<8} {mhs['nilai']:<6}")
    print()
    
def search_class(data: List[Dict], kelas: str):
    return [m for m in data if m["kelas"].upper() == kelas.upper()]

def search_name(data: List[Dict], keyword: str):
    return [m for m in data if keyword.lower() in m["nama"].lower()]

# Excec
def menu():
    data_sort = insertion(mhs, "nilai", reverse=True)
    