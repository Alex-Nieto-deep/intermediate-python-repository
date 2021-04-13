DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    allPythonDevs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    allPlatziWorker  = [worker["name"] for worker in DATA  if worker["organization"] == "Platzi"]

    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    oldPeople = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    allJavascriptDevs = list(filter(lambda worker: worker["language"] == "javascript", DATA))
    allJavascriptDevs = list(map(lambda worker: worker["name"], allJavascriptDevs))

    allRappiWorker = list(filter(lambda worker: worker["organization"] == "Rappi", DATA))
    allRappiWorker = list(map(lambda worker: worker["name"], allRappiWorker))

    young = [worker["name"] for worker in DATA if worker["age"] < 18 ]
    youngPeople = [worker | {"young": worker["age"] <= 30} for worker in DATA]


    for worker in youngPeople:
        print(worker)

if __name__ == '__main__':
    main() 