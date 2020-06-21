var tableIndex = []
var area = 64

function start(){
    
    createStructure()
    renderStructure()

}


function createStructure(){
    for (let i=0; i<(area*area); i++)  tableIndex[i] = ' ';
}


function renderStructure(){   //Render Strcture with the pixel values => create a linear table 

    let html = ' <table cellpading =0 cellspacing=0 class="table-shape">'

    for (let row=0; row<area; row++){
        html += '<tr>' //Table row => Linha
        
        for (let col=0; col<area; col++){
            const pixelIndex = col + (area * row)
            const pixelvalue = tableIndex[pixelIndex]
            
            html += '<td>'  //Table data => Coluna
            html += `<div class="table-pixel-value"> ${pixelvalue} </div>`
            html += '</td>'
        }
        html += '</tr>' 
    }
    html += '</table>'
    document.querySelector('#table-pixels').innerHTML = html //find the id (#) and put the var html into it
}


start()

