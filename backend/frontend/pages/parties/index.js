import { EnvelopeIcon, PhoneIcon } from '@heroicons/react/20/solid'
import React from "react";
import Layout from "../../components/Layout";





 
// TODO <a> tag at line 47 needs to be changed to a link to the event page (by using the slug of the event)
// TODO has to be done with the NextJs method so we are able to keep state.

const events = [
    {
    name: 'Test Event',
    description: 'This is a test event',
    type: 'Techno',
    date: '2021-10-10',
    location: 'Test Location',
    imageUrl: 'https://images.unsplash.com/photo-1616169950073-8b8f2b2b2b1c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    },
    {
    name: 'Test Event',
    description: 'This is a test event',
    type: 'Techno',
    date: '2021-10-10',
    location: 'Test Location',
    imageUrl: 'https://images.unsplash.com/photo-1616169950073-8b8f2b2b2b1c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    },
    {
    name: 'Test Event',
    description: 'This is a test event',
    type: 'Techno',
    date: '2021-10-10',
    location: 'Test Location',
    imageUrl: 'https://images.unsplash.com/photo-1616169950073-8b8f2b2b2b1c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    },
    {
    name: 'Test Event',
    description: 'This is a test event',
    type: 'Techno',
    date: '2021-10-10',
    location: 'Test Location',
    imageUrl: 'https://images.unsplash.com/photo-1616169950073-8b8f2b2b2b1c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80'
    }
]

function typeColor(type) {
    if (type === 'Techno') {
        return 'bg-blue-100 text-blue-800'
    } else if (type === 'House') {
        return 'bg-green-100 text-green-800'
    } else if (type === 'Hardstyle') {
        return 'bg-red-100 text-red-800'
    } else if (type === 'Trance') {
        return 'bg-purple-100 text-purple-800'
    } else if (type === 'Hardcore') {
        return 'bg-yellow-100 text-yellow-800'
    } else if (type === 'Drum & Bass') {
        return 'bg-indigo-100 text-indigo-800'
    } else if (type === 'Dubstep') {
        return 'bg-pink-100 text-pink-800'
    } else if (type === 'Trap') {
        return 'bg-gray-100 text-gray-800'
    } else if (type === 'Hip Hop') {
        return 'bg-orange-100 text-orange-800'
    } else if (type === 'R&B') {
        return 'bg-teal-100 text-teal-800'
    } else if (type === 'Reggae') {
        return 'bg-green-100 text-green-800'
    }
}



function Events({ events }) {
    return (
        <Layout>
            <div className='py-6 my-4 max-w-sm shadow-xl border-slate-100 border-2 text-center rounded-3xl'>
            <h1 className='text-2xl font-normal'>Upcomming Events</h1>
            </div>
            
            <ul role="list" className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 ">
                {events.map((event) => (
                <div class="flex justify-center">
                   <div class="rounded-lg shadow-lg bg-white max-w-sm transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300">
                     <a href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">
                       <img class="rounded-t-lg md:w-[350px] md:h-[200px]" src={event.imageUrl} alt=""/>
                     </a>
                     <div class="p-6">
                       <h5 class="text-gray-900 text-xl font-medium mb-2">{event.name}</h5>
                       <p class="text-gray-700 text-base mb-4">
                         {event.description}
                       </p>
                       <span className={`${typeColor(event.type)} inline-flex items-center rounded-full px-3 py-0.5 text-sm font-medium`}>
                            {event.type}
                        </span>
                     </div>
                   </div>
                 </div>
                ))}
            </ul>
        </Layout>

    )
}


// gets called at build time
export async function getStaticProps() {
    // Call to the api end point to get all parties
    const res = await fetch(`http://localhost:8000/parties`)
    const events = await res.json()

    console.log(events)

    // By returning { props: events }, the Events component
    // will receive `events` as a prop at build time
    return {
        props: {
            events 
        }
    }
    
}


export default Events; 