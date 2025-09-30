# Sistema de Gerenciamento de Veículos de uma Locadora

## Descrição do Problema

Você foi contratado para desenvolver um sistema de gerenciamento de veículos para uma locadora.  
A empresa trabalha com diferentes tipos de veículos, como **Carros, Motos e Caminhões**, cada um com características específicas.

---

## Classes a serem implementadas

### Classe `Categoria`
**Atributos**
- `nome` (string)  
- `descricao` (string)  

---

### Classe Base `Veiculo` (Abstrata)
**Atributos**
- `placa` (string) — única  
- `marca` (string)  
- `modelo` (string)  
- `valorLocacao` (decimal ou double)  
- `categoria` (objeto da classe Categoria)  
- `disponivel` (boolean) → indica se o veículo está disponível para locação  

**Métodos**
- Método abstrato `ExibirDetalhes`  

---

### Classe `Carro`
**Atributos**
- `numeroPortas` (int)  
- `automatico` (boolean)  

**Métodos**
- Implementa o método abstrato `ExibirDetalhes`  
- Exemplo de saída:  
Volkswagen Gol. 4 Portas. Ar-Condicionado. Placa: ABC 1234. Categoria: Econômico. Diária: R$ 150,00. Disponível


---

### Classe `Moto`
**Atributos**
- `cilindrada` (int)  

**Métodos**
- Implementa o método abstrato `ExibirDetalhes`  
- Exemplo de saída:  
Honda. CG 160. 160 cilindradas. Placa: GHI 9101. Categoria: Econômico. Diária: R$ 80,00. Disponível


---

### Classe `Caminhao`
**Atributos**
- `capacidadeCargaToneladas` (double)  

**Métodos**
- Implementa o método abstrato `ExibirDetalhes`  
- Exemplo de saída:  
Scania P360. 10,5 Toneladas. Placa: MNO 1314. Categoria: Utilitário. Diária: R$ 500,00. Disponível


---

### Classe `Locacao`
**Atributos**
- `identificacao` (int)  
- `veiculo` (objeto da classe Veiculo)  
- `dataInicial` (DateTime)  
- `dataFinal` (DateTime)  
- `valor` (double)  

---

## Outras Classes Necessárias

- **CadCategorias**:  
- Armazena em um vetor as categorias cadastradas  
- Métodos: inserir, retornar tamanho, retornar uma categoria por nome  

- **CadVeiculos**:  
- Armazena em um vetor os veículos cadastrados  
- Métodos: inserir, retornar tamanho, retornar veículo por placa  

- **CadLocacao**:  
- Armazena em um vetor as locações realizadas  
- Métodos: inserir, retornar tamanho, retornar locação por identificação  

- **MenuOpcoes**:  
- Gerencia o menu do software  

- **EntradaDados**:  
- Realiza leitura dos dados do teclado  

- **LeArquivoCSV**:  
- Lê arquivos CSV de categorias, veículos e locações  

- **GravaArquivoCSV**:  
- Grava arquivos CSV de categorias, veículos e locações  

---

## Regras e Requisitos Técnicos

### Funcionalidades obrigatórias:

1. **Cadastrar categoria**  
 - Criar objeto `Categoria` e armazenar no `CadCategorias`  

2. **Cadastrar veículos**  
 - Escolher tipo (carro, moto, caminhão)  
 - Informar dados + categoria (deve existir)  
 - Criar objeto e armazenar em `CadVeiculos`  

3. **Importar categorias de CSV**  
 - Exemplo `categorias.csv`:  
   ```
   nome,descrição
   Econômico,Veículos básicos e econômicos
   Executivo,Veículos confortáveis para executivos
   Utilitário,Veículos para transporte de cargas
   ```

4. **Importar veículos de CSV**  
 - Exemplo `veiculos.csv`:  
   ```
   tipo,placa,marca,modelo,valorLocacao,categoria,disponivel,atributoEspecifico1,atributoEspecifico2
   Carro,ABC1234,Volkswagen,Gol,150,Econômico,true,4,true
   Carro,DEF5678,Chevrolet,Onix,180,Executivo,true,4,false
   Moto,GHI9101,Honda,CG 160,80,Econômico,true,160,
   Moto,JKL1122,Yamaha,Factor 150,90,Executivo,false,150,
   Caminhao,MNO1314,Scania,P360,500,Utilitário,true,10.5,
   Caminhao,PQR1516,Volvo,VM270,550,Utilitário,false,12.0,
   ```

5. **Importar locações de CSV**  
 - Exemplo `locacoes.csv`:  
   ```
   Identificacao,dataInicial,dataFinal,veiculo,valor
   1,03/06/2025,08/06/2025,JKL1122,450.00
   2,05/06/2025,11/06/2025,PQR1516,3300.00
   ```

6. **Listar veículos por tipo**  
 - Exibir todos os veículos cadastrados (Carro, Moto, Caminhão) com detalhes  

7. **Realizar locação de veículo**  
 - Informar datas  
 - Listar disponíveis  
 - Calcular valor total  
 - Criar objeto `Locacao`  
 - Alterar `disponivel` para `false`  

8. **Listar todas as locações**  
 - Mostrar detalhes do veículo, datas e valor  

9. **Calcular faturamento previsto em período**  
 - Informar datas  
 - Somar valores de locações  

10. **Exportar dados para CSV**  
  - Categorias → `CATEGORIAS.CSV`  
  - Veículos → `VEICULOS.CSV`  
  - Locações → `LOCACOES.CSV`  

11. **Sair**

---

## Critérios de Avaliação

- Correta implementação das classes com encapsulamento, construtores, propriedades e `ToString`  
- Composição correta dos veículos com `Categoria`  
- Uso da classe abstrata `Veiculo`  
- Implementação da herança  
- Armazenamento em vetores  
- Implementação de processamentos exigidos  
- Importação e exportação em CSV  
- Organização, clareza e boas práticas  
