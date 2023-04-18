use mongodb::Database;
use mongodb::{Client, options::ClientOptions, options::FindOptions};
use mongodb::bson::{doc, Document};
use futures::stream::TryStreamExt;

/*
    https://github.com/mongodb/mongo-rust-driver
 */

async fn insert_new_document(db: &Database, collection_name: &str, user_id: &str) -> Result<(), Box<dyn std::error::Error>> {
    // Get a handle to a collection in database.
    let collection = db.collection::<Document>(collection_name);

    let users = vec![
        doc! { "_id": user_id, "email": user_id.to_string()+"@email.com", "verified": "true", "name": "User ".to_owned()+&user_id.to_string()},
    ];
    // Insert some documents into collection.
    collection.insert_many(users, None).await?;
    println!("Done - insert_many. user_id: {}", user_id);

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Parse a connection string into an options struct.
    let mut client_options = ClientOptions::parse("<mongo url>").await?;

    // Manually set an option.
    client_options.app_name = Some("TestApp".to_string());

    // Get a handle to the deployment.
    let client = Client::with_options(client_options)?;

    // List the names of the databases in that deployment.
    for db_name in client.list_database_names(None, None).await? {
        println!("Database: {}", db_name);
    }

    // Get a handle to a database.
    let db_name = "myApp";
    let db = client.database(db_name);

    // List the names of the collections in that database.
    for collection_name in db.list_collection_names(None).await? {
        println!("Collection: {}", collection_name);
    }

    // Insert document as row
    insert_new_document(&db, "users", "202304181430").await?;

    let collection = db.collection::<Document>("users");

    // Query the books in the collection with a filter and an option.
    let filter = doc! { "name": "Test User" };
    let find_options = FindOptions::builder().sort(doc! { "_id": 1 }).build();
    let mut cursor = collection.find(filter, find_options).await?;

    // Iterate over the results of the cursor, print the json doc.
    while let Some(row) = cursor.try_next().await? {
        println!("row: {:?}", row);
    }

    Ok(())
}