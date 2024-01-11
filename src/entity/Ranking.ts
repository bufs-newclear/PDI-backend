import { Entity, PrimaryGeneratedColumn, Column, OneToOne, JoinColumn } from "typeorm"
import { Meal } from "./Meal";

export enum rankScope {
    Weekly = "weekly",
    Daily = "daily",
    Monthly = "monthly",
    Quarter = "quarter",
    Half = "half",
    Yearly = "yearly",
};

@Entity()
export class Ranking {
    @PrimaryGeneratedColumn()
    id: number;
    
    @Column()
    createdAt: string;

    @OneToOne(() => Meal, (meal) => meal.id)
    meal: Meal

    @Column({ type: 'enum', enum: rankScope, default: rankScope.Weekly })
    rankScope: rankScope;

    @Column()
    likeCount: number;
}