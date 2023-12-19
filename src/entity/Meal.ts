import { Entity, PrimaryGeneratedColumn, Column } from "typeorm"

export enum MealType {
    Morning = "morning",
    Lunch = "lunch",
    Employee = "employee",
};

@Entity()
export class Meal {
    @PrimaryGeneratedColumn()
    id: number;
    
    @Column()
    createdAt: string;

    @Column()
    name: string;

    @Column({ type: 'enum', default: MealType.Lunch })
    mealType: MealType;
    
    @Column({ nullable: true })
    place?: string;

    @Column({ nullable: true })
    imagePath?: string;

    @Column({ nullable: true })
    price: number;

    @Column({ nullable: true })
    isAvailable: boolean;
}
