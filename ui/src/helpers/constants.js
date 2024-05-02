const BASE_URL = "https://core.verse-stg.tam.run";
const TENANT = process.env.NODE_ENV == "production" ? "river-admin" : "";
export { BASE_URL, TENANT };
