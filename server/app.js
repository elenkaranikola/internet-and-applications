const express = require('express');
const app = express();
const cors = require('cors');
const dotenv = require('dotenv');
const bodyParser= require('body-parser')
dotenv.config();
app.use(express.static(__dirname))

app.get('/',function(req,res){

  res.sendFile(__dirname + "/index.html")

});

const dbService = require('./dbService');

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended : false }));


// read
app.get('/getAll', (request, response) => {
    const db = dbService.getDbServiceInstance();

    const result = db.getAllData();
    
    result
    .then(data => response.json({data : data}))
    .then(console.log('getAll here'))
    .catch(err => console.log(err));
})

app.get('/showAll', (request, response) => {
    const db = dbService.getDbServiceInstance();

    const result = db.CountData();
    
    result
    .then(data => response.json({data : data}))
    .then(console.log('showAll here'))
    .catch(err => console.log(err));
    
})

app.get('/search/:name', (request, response) => {
    const { name } = request.params;
    const db = dbService.getDbServiceInstance();

    const result = db.searchByName(name);
    
    result
    .then(data => response.json({data : data}))
    .catch(err => console.log(err));
})


// create
//app.post('/insert', (request, response) => {
//    const { name } = request.body;
//    const db = dbService.getDbServiceInstance();
//    
//    const result = db.insertNewName(name);
//
//    result
//    .then(data => response.json({ data: data}))
//    .catch(err => console.log(err));
//});



// update
//app.patch('/update', (request, response) => {
//    const { id, name } = request.body;
//    const db = dbService.getDbServiceInstance();
//
//    const result = db.updateNameById(id, name);
//    
//    result
//    .then(data => response.json({success : data}))
//    .catch(err => console.log(err));
//});

// delete
//app.delete('/delete/:id', (request, response) => {
//    const { id } = request.params;
//    const db = dbService.getDbServiceInstance();
//
//    const result = db.deleteRowById(id);
//    
//    result
//    .then(data => response.json({success : data}))
//    .catch(err => console.log(err));
//});


app.listen(process.env.PORT, () => console.log('app is running'));