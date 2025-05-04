const { writeToSheet } = require("./sheetService");

async function routes(app){
    app.get("/", (request, reply) => {
        reply.status(200).send()
    })

    app.post("/", async (request, reply) => {
        const studentsListBody = request.body
    
        const spreadsheetObject = await writeToSheet(process.env.WORKSHEET, studentsListBody)
    
        console.log(`spreadsheetObject: ${spreadsheetObject}`)
    
        reply.status(200).send(spreadsheetObject)
    })
}

module.exports = routes