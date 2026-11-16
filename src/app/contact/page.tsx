import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact Us | MGBW Group",
  description:
    "Get in touch with MGBW Group. Reach us at our head office in Mysore.",
};

export default function ContactPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gray-900 text-white py-20 text-center">
        <h1 className="text-4xl md:text-5xl font-bold mb-4">Contact Us</h1>
        <p className="text-lg font-light opacity-80">
          We&apos;d love to hear from you
        </p>
      </section>

      <section className="py-20 px-4 bg-white">
        <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
          {/* Contact Form */}
          <div>
            <h2 className="text-2xl font-bold mb-6">Send us a Message</h2>
            <form className="space-y-6">
              <div>
                <label
                  htmlFor="name"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  className="w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-pink-500"
                  placeholder="Your Name"
                />
              </div>
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  className="w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-pink-500"
                  placeholder="Your Email"
                />
              </div>
              <div>
                <label
                  htmlFor="message"
                  className="block text-sm font-medium text-gray-700 mb-1"
                >
                  Message
                </label>
                <textarea
                  id="message"
                  name="message"
                  rows={5}
                  className="w-full border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-pink-500"
                  placeholder="Your Message"
                />
              </div>
              <button
                type="submit"
                className="bg-pink-600 text-white px-8 py-3 rounded-full hover:bg-pink-700 transition font-semibold"
              >
                Send Message
              </button>
            </form>
          </div>

          {/* Contact Info & Map */}
          <div>
            <h2 className="text-2xl font-bold mb-6">Get in Touch</h2>
            <div className="space-y-4 text-gray-600 mb-8">
              <div>
                <h3 className="font-semibold text-gray-900">Address</h3>
                <p>Head Office, Vinoba Road, Mysore - 570005</p>
              </div>
              <div>
                <h3 className="font-semibold text-gray-900">Email</h3>
                <a
                  href="mailto:customercare@mgbw501.com"
                  className="text-pink-600 hover:underline"
                >
                  customercare@mgbw501.com
                </a>
              </div>
              <div>
                <h3 className="font-semibold text-gray-900">Phone</h3>
                <a
                  href="tel:08212420241"
                  className="text-pink-600 hover:underline"
                >
                  0821-2420241
                </a>
              </div>
            </div>

            {/* Map Embed */}
            <div className="rounded-xl overflow-hidden shadow-md">
              <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3898.0!2d76.65!3d12.31!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTLCsDE4JzM2LjAiTiA3NsKwMzknMDAuMCJF!5e0!3m2!1sen!2sin!4v1"
                width="100%"
                height="300"
                style={{ border: 0 }}
                allowFullScreen
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                title="MGBW Group Location"
              />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
