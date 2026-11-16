import Image from "next/image";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "J&G Agarbatti | Premium Incense Sticks & Prayer Essentials",
  description:
    "Premium incense sticks inspired by devotion, meticulously crafted using natural ingredients for a divine experience.",
};

const features = [
  "Long-Lasting Fragrance",
  "Eco-Friendly Ingredients",
  "Variety of Fragrances",
  "Soothing & Relaxing Aroma",
];

const fragrances = [
  "Lavender",
  "Champa",
  "Jasmine",
  "Rose",
  "Mogra",
  "Sandalwood",
  "Vanamali",
  "Bell 3 in 1",
  "Temple",
  "Divine Aura",
  "Wild Flower",
  "Wonder Flower",
];

const whyPartner = [
  "Flexible volume-based pricing",
  "Custom fragrance options for high-demand regions",
  "Packaging tailored for retail and religious resale",
  "Strong customer retention and recurring orders",
  "Clean, compliant manufacturing and supply chain",
];

export default function JGAgarbattiPage() {
  return (
    <>
      {/* Hero */}
      <section className="relative h-[70vh] flex items-center justify-center bg-gray-900">
        <div className="absolute inset-0">
          <Image
            src="/images/business/jg/jg-hero.jpg"
            alt="J&G Agarbatti"
            fill
            className="object-cover opacity-40"
            priority
          />
        </div>
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">
            J&amp;G AGARBATHIES
          </h1>
          <p className="text-xl font-light mb-2">
            Fragrance Rooted in Tradition.
          </p>
          <p className="text-lg opacity-80">Crafted for the Soul.</p>
          <p className="text-base opacity-70 mt-4 max-w-2xl mx-auto">
            Premium incense sticks inspired by devotion, meticulously crafted
            using natural ingredients for a divine experience.
          </p>
          <Link
            href="/contact"
            className="inline-block mt-8 px-8 py-3 bg-pink-600 text-white rounded-full hover:bg-pink-700 transition"
          >
            Become a Distributor
          </Link>
        </div>
      </section>

      {/* Features Bar */}
      <section className="bg-pink-600 text-white py-8">
        <div className="max-w-4xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          {features.map((f) => (
            <div key={f} className="text-sm font-medium">{f}</div>
          ))}
        </div>
      </section>

      {/* About */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-2">About Us</h2>
          <p className="text-pink-600 text-xl mb-8">
            A Tradition of Aromatic Excellence
          </p>
          <div className="text-gray-600 leading-relaxed space-y-4">
            <p>
              J&amp;G Agarbatti has emerged as a leading name in incense stick
              production and distribution across India &amp; Abroad. We combine
              time-honored craftsmanship with modern practices to deliver
              superior-quality incense that enriches spiritual rituals and daily
              environments.
            </p>
            <p>
              Guided by our values of purity, sustainability, and devotion, we
              use only the finest authentic elements, creating signature blends
              that are both calming and enduring.
            </p>
          </div>
        </div>
      </section>

      {/* What Makes Us Different */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">
            What Makes Us Different
          </h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {[
              "Use of natural resins, essential oils, and eco-friendly bases",
              "Fragrances inspired by Indian tradition and spiritual needs",
              "Consistent burn time and rich aromatic throw",
              "Sustainable production and packaging",
              "Compliance with national quality standards",
            ].map((item) => (
              <div
                key={item}
                className="flex items-center gap-3 p-4 bg-white rounded-lg shadow-sm"
              >
                <span className="text-pink-600 font-bold text-xl">✓</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Product Range */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">Product Experience</h2>
          <p className="text-gray-600 mb-6">
            J&amp;G incense sticks are designed to complement every setting, from
            homes and prayer rooms to temples and meditation centers.
          </p>
          <div className="grid sm:grid-cols-3 gap-4 mb-12">
            {[
              "Regular Incense Sticks",
              "Premium Long-Lasting Series",
              "Ritual and Festival Collections",
            ].map((item) => (
              <div
                key={item}
                className="bg-gray-50 rounded-xl p-6 text-center font-semibold"
              >
                {item}
              </div>
            ))}
          </div>

          {/* Fragrances Grid */}
          <h3 className="text-2xl font-bold mb-6 text-center">
            Fragrance of Faith
          </h3>
          <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3">
            {fragrances.map((f) => (
              <div
                key={f}
                className="bg-pink-50 rounded-lg p-3 text-center text-sm font-medium text-pink-800"
              >
                {f}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Partner */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">Why Partner with J&amp;G</h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {whyPartner.map((item) => (
              <div
                key={item}
                className="flex items-center gap-3 p-4 bg-white rounded-lg shadow-sm"
              >
                <span className="text-pink-600 font-bold text-xl">✓</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-pink-600 text-white text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">
          Let&apos;s Spread Fragrance Together
        </h2>
        <p className="mb-6 opacity-90 max-w-xl mx-auto">
          Fragrance with purpose. Partnership with integrity.
        </p>
        <Link
          href="/contact"
          className="inline-block px-8 py-3 bg-white text-pink-600 rounded-full font-semibold hover:bg-gray-100 transition"
        >
          Contact Us
        </Link>
      </section>
    </>
  );
}
