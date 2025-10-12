# data
mahasiswa = [
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
def insertion(data):
    for i in range (1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j]["nilai"] < key["nilai"]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def merge_srt(data):
    if len(data) < 1:
        return data
    mid = len(data) // 2
    left = merge_srt(data[:mid])
    right = merge_srt(data[mid:])
    return merge_srt(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["nilai"] > right[j]["nilai"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Algotihm
def binary(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["nilai"] == target:
            return mid
        elif data[mid]["nilai"] < target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["nim"] == target:
            return mid
        elif data[mid]["nim"] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# utility
def show_data(data):
    print("\n{:<4} {:<20} {:<10} {:<8} {:<6}".format("No", "Nama", "NIM", "Kelas", "Nilai"))
    print("=" * 55)
    for i, mhs in enumerate(data, 1):
        print(f"{i:<4} {mhs['nama']:<20} {mhs['nim']:<10} {mhs['kelas']:<8} {mhs['nilai']:<6}")
    print()
    
def search_class(data, kelas):
    result = [mhs for mhs in data if mhs["kelas"].lower() == kelas.lower()]
    if result:
        print(f"\nMahasiswa di kelas {kelas.upper()}:")
        for m in result:
            print(f"- {m['nama']} ({m['nim']})")
    else:
        print(f"Tidak ada mahasiswa di kelas {kelas}")

# Excec
def menu():
    show = show_data(mahasiswa)
    
    
            
if __name__ == "__main__":
    menu()