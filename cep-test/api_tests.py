import json
import urllib.error
import urllib.request

BASE_URL = "https://cdn.apicep.com/file/apicep/{}.json"

cases = [
    {
        "id": "CT01",
        "description": "Fluxo básico - CEP válido",
        "cep": "06233-030",
        "expected_status": 200,
        "expected_fields": {
            "code": "06233-030",
            "state": "SP",
            "city": "Osasco",
            "address": "Rua Paula Rodrigues",
        },
    },
    {
        "id": "CT02",
        "description": "Fluxo alternativo - outro CEP válido",
        "cep": "01001-000",
        "expected_status": 200,
        "expected_fields": {
            "code": "01001-000",
            "state": "SP",
            "city": "São Paulo",
            "district": "Sé",
        },
    },
    {
        "id": "CT03",
        "description": "Fluxo de exceção - CEP inválido",
        "cep": "99999-999",
        "expected_status": 404,
        "expected_fields": {},
    },
]


def run_case(case):
    url = BASE_URL.format(case["cep"])
    print(f"\n=== {case['id']} - {case['description']} ===")
    print(f"URL: {url}")

    try:
        response = urllib.request.urlopen(url)
        body = response.read().decode("utf-8")
        status = response.getcode()
        print(f"Status HTTP: {status}")
        if status != case["expected_status"]:
            print(f"FALHA: status esperado {case['expected_status']} mas recebeu {status}")
            return False

        if status == 200:
            data = json.loads(body)
            for field, expected in case["expected_fields"].items():
                actual = data.get(field)
                print(f"  {field}: {actual}")
                if actual != expected:
                    print(f"FALHA: {field} esperado '{expected}' mas recebeu '{actual}'")
                    return False
            print("SUCESSO: todos os campos esperados foram validados")
        else:
            print("SUCESSO: status de exceção esperado retornado")
        return True

    except urllib.error.HTTPError as error:
        status = error.getcode()
        print(f"Status HTTP: {status}")
        if status != case["expected_status"]:
            print(f"FALHA: status esperado {case['expected_status']} mas recebeu {status}")
            return False
        print("SUCESSO: exceção esperada recebida")
        return True
    except Exception as exc:
        print(f"FALHA inesperada: {exc}")
        return False


if __name__ == "__main__":
    results = []
    for case in cases:
        ok = run_case(case)
        results.append((case["id"], ok))

    print("\n=== Resultado geral ===")
    for case_id, ok in results:
        print(f"{case_id}: {'PASS' if ok else 'FAIL'}")
