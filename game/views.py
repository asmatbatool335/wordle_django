import random
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import Counter

# A simple list of 5-letter words (expand as needed)
WORD_LIST = [
    'CRANE', 'PLANT', 'BRAVE', 'SHINE', 'GHOST', 'WORDS', 'APPLE', 'MOUSE', 'TRAIN', 'SHEET',
    'CLEAN', 'BRAIN', 'SUGAR', 'WATER', 'EARTH', 'HEART', 'SWEET', 'NIGHT', 'LIGHT', 'SOUND'
]

MAX_GUESSES = 6

def get_solution(request):
    if 'solution' not in request.session:
        request.session['solution'] = random.choice(WORD_LIST)
    return request.session['solution']

def wordle(request):
    # Ensure a solution is set in the session
    get_solution(request)
    # Reset guesses for a new game
    request.session['guesses'] = []
    return render(request, 'game/wordle.html')

def new_game(request):
    request.session.flush()  # Clear the session (removes solution and guesses)
    return redirect('wordle')

@csrf_exempt
def check_guess(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        guess = data.get('guess', '').upper()
        solution = get_solution(request)
        guesses = request.session.get('guesses', [])
        # Only add non-empty guesses
        if guess:
            guesses.append(guess)
            request.session['guesses'] = guesses
        result = ['absent'] * 5
        solution_chars = list(solution)
        guess_chars = list(guess)

        # First pass: mark correct (green)
        for i in range(5):
            if guess_chars[i] == solution_chars[i]:
                result[i] = 'correct'
                solution_chars[i] = None  # Mark as used
                guess_chars[i] = None     # Mark as used

        # Count remaining unmatched letters in the solution
        remaining = Counter([c for c in solution_chars if c is not None])

        # Second pass: mark present (yellow)
        for i in range(5):
            if guess_chars[i] is not None and remaining[guess_chars[i]] > 0:
                result[i] = 'present'
                remaining[guess_chars[i]] -= 1
        is_correct = guess == solution
        out_of_guesses = len(guesses) >= MAX_GUESSES and not is_correct
        reveal_solution = is_correct or out_of_guesses or data.get('reveal')
        return JsonResponse({'result': result, 'is_correct': is_correct, 'solution': solution if reveal_solution else None})
    return JsonResponse({'error': 'Invalid request'}, status=400)
