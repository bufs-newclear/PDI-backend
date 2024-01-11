import axios from 'axios';
import * as cheerio from 'cheerio';
import jsdom from 'jsdom';
import { format, isBefore, subMinutes } from 'date-fns';

class BUFSMeals {
    private static WEEKLY_MEAL_URL = 'http://www.bufs.ac.kr/bbs/my/ajax.view.skin.php?bo_table=weekly_meal&wr_id=1';
    private lastUpdated: Date | null;
    private weeklyMeals: any[];

    constructor(fetchOnInit: boolean = true) {
        this.lastUpdated = null;
        this.weeklyMeals = [];

        if (fetchOnInit) {
            this.refresh();
        }
    }

    private isValid(): boolean {
        return this.lastUpdated !== null && isBefore(subMinutes(new Date(), 30), this.lastUpdated);
    }

    public async getWeekly() {
        if (!this.isValid()) {
            await this.refresh();
        }
        return this.weeklyMeals;
    }

    public async getDaily(date: Date | null = null) {
        if (!this.isValid()) {
            await this.refresh();
        }

        return this.weeklyMeals.find(day => day.date === date) || null;
    }

    private async refresh() {
        try {
            const response = await axios.get(BUFSMeals.WEEKLY_MEAL_URL);
            const dom = new JSDOM(response.data);
            const document = dom.window.document;
            const tbls = Array.from(document.querySelectorAll('table.__se_tbl'));
            const weeklyMeals: any[] = [];

            // [여기에 나머지 파싱 로직을 추가하세요]
            

            this.weeklyMeals = weeklyMeals;
            this.lastUpdated = new Date();
        } catch (error) {
            throw new Error(`Error fetching page: ${error}`);
        }
    }
}