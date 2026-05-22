Feature: Busca de endereço por CEP
  Como gestor
  Quero utilizar uma API pública
  Para que eu possa realizar testes funcionais de busca de CEP

  Scenario: Fluxo básico - buscar endereço por CEP válido
    Given a API de busca de CEP disponível em "https://cdn.apicep.com/file/apicep/06233-030.json"
    When eu realizo uma requisição GET para a URL
    Then o retorno deve ser HTTP 200
    And o corpo deve estar em JSON
    And o campo "code" deve ser "06233-030"
    And o campo "state" deve ser "SP"
    And o campo "city" deve ser "Osasco"
    And o campo "address" deve ser "Rua Paula Rodrigues"

  Scenario: Fluxo alternativo - buscar outro CEP válido com caracteres acentuados
    Given a API de busca de CEP disponível em "https://cdn.apicep.com/file/apicep/01001-000.json"
    When eu realizo uma requisição GET para a URL
    Then o retorno deve ser HTTP 200
    And o corpo deve estar em JSON
    And o campo "code" deve ser "01001-000"
    And o campo "state" deve ser "SP"
    And o campo "city" deve ser "São Paulo"
    And o campo "district" deve ser "Sé"

  Scenario: Fluxo de exceção - buscar CEP inválido
    Given a API de busca de CEP disponível em "https://cdn.apicep.com/file/apicep/99999-999.json"
    When eu realizo uma requisição GET para a URL
    Then o retorno deve ser HTTP 404
    And a requisição deve ser tratada como CEP não encontrado
