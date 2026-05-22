# Desafio de Testes de API - Busca de CEP

Este repositório contém os artefatos do desafio de testes de software usando a API pública de busca de CEP disponível em:

`https://cdn.apicep.com/file/apicep/[cep].json`

## Conteúdo

- `test-cases/CEP-Search.feature`: Casos de teste escritos em Gherkin.
- `postman_collection.json`: Coleção Postman com chamadas de teste e validações.
- `api_tests.py`: Script de validação simples em Python para executar os mesmos cenários.
- `evidence/CT01_FB_BuscaCEP.txt`: Evidência do fluxo básico.
- `evidence/CT02_FA_BuscaCEP_Alternativo.txt`: Evidência do fluxo alternativo.
- `evidence/CT03_FE_BuscaCEP_Excecao.txt`: Evidência do fluxo de exceção.

## Como executar

1. Execute o script Python:

   ```bash
   python api_tests.py
   ```

2. Abra `postman_collection.json` no Postman ou Insomnia para executar os testes.
