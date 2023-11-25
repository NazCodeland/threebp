import pgPromise from "pg-promise";

// Initialize pg-promise and connect to your database
const pgp = pgPromise();
const db = pgp({
	host: "ep-shiny-pond-80219216.us-east-2.aws.neon.tech",
	port: 5432,
	database: "neondb",
	user: "tsxsectors",
	password: "Fl0i5WKCQmZg",
	ssl: {
		rejectUnauthorized: false,
	},
});

export async function upload_to_db(
	industry: string,
	rows: { symbol: any; name: any }[]
) {
	// Define the table name
	const tableName = industry.toLowerCase();

	// Check if the table exists, and if not, create it
	const createTableQuery = `
		CREATE TABLE IF NOT EXISTS ${tableName} (
			symbol TEXT,
			name TEXT
		)
	`;
	await db.none(createTableQuery);

	console.log(industry, rows);

	// Use pg-promise helper to create a multi-row insert statement
	const insert = pgp.helpers.insert(rows, ["symbol", "name"], tableName);

	// Execute the query
	await db.none(insert);
}

export async function upload_to_db_barchart(industryEquities: any) {
	// Create table
	await db.none(
		"CREATE TABLE IF NOT EXISTS industry_equities(industry VARCHAR(50), equities JSONB)"
	);

	// Insert data into the table
	for (let industry in industryEquities) {
		await db.none("INSERT INTO industry_equities VALUES($1, $2)", [
			industry,
			industryEquities[industry],
		]);
	}

	console.log("Data inserted successfully!");
}
