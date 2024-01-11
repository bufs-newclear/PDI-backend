import { AppDataSource } from "../data-source";
import { NextFunction, Request, Response } from "express";
import { User } from "../entity/User";
import { Meal } from "../entity/Meal";

export class MealController {

    private userRepository = AppDataSource.getRepository(User);
    private mealRepository = AppDataSource.getRepository(Meal);

    async all(request: Request, response: Response, next: NextFunction) {
        return this.mealRepository.find();
    }

    async one(request: Request, response: Response, next: NextFunction) {
        const id = parseInt(request.params.id);


        const meal = await this.mealRepository.findOne({
            where: { id }
        });

        if (!meal) {
            return "unregistered meal";
        }
        return meal;
    }

    async today(request: Request, response: Response, next: NextFunction) {
        // TODO

        const today = '';  // TODO
        const meals = await this.mealRepository.find({
            where: { createdAt: today }
        });

        meals.forEach(meal => {
            const reactions = await this.mealRepository.find({
                where: { meal: }
            })
        });
    }

    async save(request: Request, response: Response, next: NextFunction) {
        const { firstName, lastName, age } = request.body;

        const user = Object.assign(new User(), {
            firstName,
            lastName,
            age
        });

        return this.userRepository.save(user);
    }

    async remove(request: Request, response: Response, next: NextFunction) {
        const id = parseInt(request.params.id);

        let userToRemove = await this.userRepository.findOneBy({ id });

        if (!userToRemove) {
            return "this user not exist";
        }

        await this.userRepository.remove(userToRemove);

        return "user has been removed";
    }

}