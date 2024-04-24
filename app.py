from flask import Flask, render_template, jsonify
from requests import get

app = Flask(__name__)

@app.route('/scores', methods=['GET'])
def get_scores():
    try:
        response = get("http://193.164.149.85:5000/scores")
        result = response.json()[0]
        # return jsonify(result[0])
        final_winner = result['final_winner']
        final_winner_score = result['final_winner_score']
        id = result['id']
        name_team_1 = result['name_team_1']
        name_team_2 = result['name_team_2']
        progress_bar_state = result['progress_bar_state']
        score_team_1 = result['score_team_1']
        score_team_2 = result['score_team_2']
        score_teams = result['score_teams']
        state_of_vidget = result['state_of_vidget']
        team_1_score_street_1 = result['team_1_score_street_1']
        team_1_score_street_2 = result['team_1_score_street_2']
        team_1_score_street_3 = result['team_1_score_street_3']
        team_2_score_street_1 = result['team_2_score_street_1']
        team_2_score_street_2 = result['team_2_score_street_2']
        team_2_score_street_3 = result['team_2_score_street_3']
        team_score_street_main = result['team_score_street_main']
        timer = result['timer']
        timer_end = result['timer_end']
        timer_start = result['timer_start']
        return jsonify(final_winner=final_winner, final_winner_score=final_winner_score, id=id, name_team_1=name_team_1, name_team_2=name_team_2, progress_bar_state=progress_bar_state, score_team_1=score_team_1, score_team_2=score_team_2, score_teams=score_teams, state_of_vidget=state_of_vidget, team_1_score_street_1=team_1_score_street_1, team_1_score_street_2=team_1_score_street_2, team_1_score_street_3=team_1_score_street_3, team_2_score_street_1=team_2_score_street_1, team_2_score_street_2=team_2_score_street_2, team_2_score_street_3=team_2_score_street_3, team_score_street_main=team_score_street_main, timer=timer, timer_end=timer_end, timer_start=timer_start)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error fetching data"})

@app.route('/')
def index():
    response = get("http://193.164.149.85:5000/scores")
    result = response.json()[0]
    return render_template('index.html', result=result)
    # return render_template('tmp.html', result=result)
    

if __name__ == '__main__':
    app.run(debug=True)
