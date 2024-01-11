import { Entity, PrimaryGeneratedColumn, Column, OneToOne, JoinColumn } from "typeorm"
import { Meal } from "./Meal";
import { User } from "./User";

@Entity()
export class Reaction {
    @PrimaryGeneratedColumn()
    id: number;
    
    @Column()
    createdAt: string;

    @OneToOne(() => User, (user) => user.id)
    user: User

    @OneToOne(() => Meal, (meal) => meal.id)
    meal: Meal

    @Column()
    type: string;
}