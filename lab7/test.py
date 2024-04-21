from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)


async def process_event(event):
    # Здесь должна быть ваша логика обработки события
    await asyncio.sleep(2)  # Просто имитация обработки события
    return f"Event '{event}' processed successfully"


@app.route('/events', methods=['POST'])
async def handle_event():
    event_data = await request.json()
    event = event_data.get('event')
    if event:
        response = await process_event(event)
        return jsonify({'message': response}), 200
    else:
        return jsonify({'error': 'Event data not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
