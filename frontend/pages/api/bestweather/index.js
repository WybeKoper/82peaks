import {mountains} from "../../../data/mountains"

export default function handler(req, res) {
    console.log(req["query"]["startDate"])
    console.log(req["query"]["endDate"])
    res.status(200).json(mountains)
}