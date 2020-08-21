const mysql = require('mysql');

const pool = mysql.createPool({
    connectionLimit : 100, //important
    host     : 'localhost',
    user     : 'root',
    password : 'eleni123',
    database : 'InterntAndApplications',
    debug    :  false
});

// query rows in the table

function queryRow(userName) {
    //let selectQuery = 'SELECT * FROM ?? WHERE ?? = ?';  
    let selectQuery = 'SELECT month(publish_time),count(journal) FROM ?? WHERE ?? = ? GROUP BY month(publish_time) ORDER BY month(publish_time)';  
    let query = mysql.format(selectQuery,["general","journal", userName]);
    // query = SELECT * FROM `todo` where `user` = 'shahid'
    pool.query(query,(err, data) => {
        if(err) {
            console.error(err);
            return;
        }
        // rows fetch
        //return (data);
        console.log(data);
    });
}

// timeout just to avoid firing query before connection happens

setTimeout(() => {
    // call the function
    // select rows
    queryRow('PLoS One');
},5000);
