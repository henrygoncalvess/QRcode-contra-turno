const { google } = require("googleapis");

async function writeToSheet(range, sheetData) {
    const auth = new google.auth.GoogleAuth({
        keyFile: './google.json',
        scopes: ['https://www.googleapis.com/auth/spreadsheets']
    });

    const service = google.sheets({version: 'v4', auth: auth});

    const spreadsheetId = process.env.SHEET_ID
    const valueInputOption = 'USER_ENTERED'
    const resource = {
        values: sheetData
    }
    
    try {
        const spreadsheet = await service.spreadsheets.values.update({
            spreadsheetId,
            range,
            valueInputOption,
            resource
        });

        return spreadsheet
    } catch (err) {
        throw err;
    }
}

module.exports = { writeToSheet }