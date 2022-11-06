

const EventCard = ({event}) => {
    return(
    <>
    {/* create a grid list with all the events using tailwind css */}
        <div className="grid grid-cols-3" key={event.trcid}>
            <div class="rounded overflow-hidden shadow-lg">
            <img class="w-full" src={event.media[0].url} alt="Mountain"></img>
            <div class="px-6 py-4">
                <div class="font-bold text-xl mb-2">{event.title}</div>
                <p class="text-gray-700 text-base">
                {event.details.nl.shortdescription}
                </p>
            </div>
            <div class="px-6 pt-4 pb-2">
                <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
                <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
                <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
            </div>
            </div>
        </div>
)
    </>

    )
}

export default EventCard
