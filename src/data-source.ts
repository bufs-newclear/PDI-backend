import "reflect-metadata"
import { DataSource } from "typeorm"
// import { User } from "./entity/User"
import { User, Meal, Reaction, Ranking } from "./entity/index"

export const AppDataSource = new DataSource({
    type: "postgres",
    host: "localhost",
    port: 5432,
    username: "test",
    password: "test",
    database: "test",
    synchronize: true,
    logging: false,
    entities: [User, Meal, Reaction, Ranking],
    migrations: [],
    subscribers: [],
})
