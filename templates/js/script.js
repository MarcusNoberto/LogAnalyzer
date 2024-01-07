function generateTable(logsData) {
    const cabecalho = {
        title: ['IP', 'HORÁRIO', 'MENSAGEM', 'NÍVEL', 'DESCRIÇÃO']
    };

    const headerRow = `<thead><tr>${cabecalho.title.map(title => `<th>${title}</th>`).join('')}</tr></thead>`;

    const tableRows = logsData.map(log => `
        <tr>
            <td>${log.ip_address}</td>
            <td>${log.timestamp}</td>
            <td>${log.message}</td>
            <td>${log.level}</td>
            <td class="description">${log.description}</td>
        </tr>`
    );

    return `<table>${headerRow}<tbody>${tableRows.join('')}</tbody></table>`;
}

function tablePaginate(logsData, startIndex, endIndex) {
    const tabelasExibidas = logsData.slice(startIndex, endIndex);
    return generateTable(tabelasExibidas);
}

const hype = {
    get(item) {
        return document.querySelector(item);
    }
};

let quantidadePorPagina = 1;
const estado = {
    pagina: 1,
    quantidadePorPagina,
    numerosPorPagina: 1,
};

const controles = {
    next() {
        estado.pagina++;
        if (estado.pagina > estado.totalPagina) {
            estado.pagina--;
        }
        update();
    },
    prev() {
        estado.pagina--;
        if (estado.pagina < 1) {
            estado.pagina++;
        }
        update();
    },
    createListeners() {
        hype.get('.next').addEventListener('click', () => {
            controles.next();
        });
        hype.get('.prev').addEventListener('click', () => {
            controles.prev();
        });
    }
};

function update() {
    const startIndex = (estado.pagina - 1) * estado.quantidadePorPagina;
    const endIndex = startIndex + estado.quantidadePorPagina;

    const tabelasContainer = hype.get('.tabela');
    tabelasContainer.innerHTML = tablePaginate(logsData, startIndex, endIndex);

    const numerosPaginas = hype.get('.numbers');
    numerosPaginas.innerHTML = '';

    const totalPages = estado.totalPagina;
    const currentPage = estado.pagina;

    const startPage = Math.max(1, currentPage - Math.floor(estado.numerosPorPagina / 2));
    const endPage = Math.min(totalPages, startPage + estado.numerosPorPagina - 1);

    for (let i = startPage; i <= endPage; i++) {
        const numeroPagina = document.createElement('div');
        numeroPagina.textContent = i;
        numeroPagina.classList.add('page-number');

        if (i === currentPage) {
            numeroPagina.classList.add('active');
        }

        numeroPagina.addEventListener('click', function () {
            estado.pagina = i;
            update();
        });

        numerosPaginas.appendChild(numeroPagina);
    }
}

// QuantidadeTabela será inicializado no carregamento da página usando dados do servidor (logsData)
update();

controles.createListeners();
