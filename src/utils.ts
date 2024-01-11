import moment = require("moment-timezone");

const timezone = 'Asia/Seoul';

// 2038-12-31 형식의 날짜를 반환합니다.
export function datestring() {
    // 현재 날짜와 시간을 해당 timezone으로 가져옵니다.
    const currentDateTime = moment().tz(timezone);

    // 2000-12-31 형식의 문자열로 변환합니다.
    return currentDateTime.format('YYYY-MM-DD');

}