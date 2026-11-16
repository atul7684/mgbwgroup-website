import Image from "next/image";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Mangalore Ganesh Beedi Works | Iconic 501 Ganesh Beedi Since 1940",
  description:
    "From India to the world, premium handcrafted beedis backed by tradition, consistency, and quality.",
};

const stats = [
  { number: "500+", label: "Distributors" },
  { number: "4+", label: "Export Countries" },
  { number: "80+", label: "Years of Business" },
  { number: "100%", label: "Industry Compliant" },
];

const globalReach = [
  {
    region: "North America",
    desc: "Established strong distribution networks across Caribbean islands with focus on premium tobacco products.",
  },
  {
    region: "Southeast Asia",
    desc: "Strategic hub for Southeast Asian markets with modern logistics and compliance systems.",
  },
  {
    region: "Europe",
    desc: "Gateway to European markets with emphasis on quality assurance and regulatory compliance.",
  },
  {
    region: "Africa",
    desc: "Africa operations focusing on premium distribution and regulatory compliance.",
    comingSoon: true,
  },
  {
    region: "Middle East",
    desc: "Upcoming expansion into Gulf markets with tailored product offerings and cultural considerations.",
    comingSoon: true,
  },
];

const whyChooseUs = [
  "80+ years of brand credibility",
  "Efficient turnaround time for bulk orders",
  "Custom labeling and packaging options",
  "Strong distributor margins",
  "Dedicated account management team",
  "Transparent business processes",
];

export default function GaneshBeediPage() {
  return (
    <>
      {/* Hero */}
      <section className="relative h-[70vh] flex items-center justify-center bg-gray-900">
        <div className="absolute inset-0">
          <Image
            src="/images/business/ganeshbeedi/ganeshbeedi-hero.jpg"
            alt="Mangalore Ganesh Beedi Works"
            fill
            className="object-cover opacity-40"
            priority
          />
        </div>
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">
            Mangalore Ganesh Beedi Works
          </h1>
          <p className="text-lg font-light mb-2">
            Tradition of trust since 1940
          </p>
          <p className="text-base opacity-80 max-w-2xl mx-auto">
            From India to the world, premium handcrafted beedis backed by
            tradition, consistency, and quality.
          </p>
          <Link
            href="/contact"
            className="inline-block mt-8 px-8 py-3 bg-pink-600 text-white rounded-full hover:bg-pink-700 transition"
          >
            Partner With Us
          </Link>
        </div>
      </section>

      {/* Stats Bar */}
      <section className="bg-pink-600 text-white py-8">
        <div className="max-w-4xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
          {stats.map((s) => (
            <div key={s.label}>
              <div className="text-2xl font-bold">{s.number}</div>
              <div className="text-sm opacity-90">{s.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* About */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-2">About Us</h2>
          <p className="text-pink-600 text-xl mb-8">Scaling Success</p>
          <div className="text-gray-600 leading-relaxed space-y-4">
            <p>
              Mangalore Ganesh Beedi Works has been a symbol of quality and
              tradition for more than eight decades. Renowned for its flagship
              brand, &ldquo;501 Mangalore Ganesh Beedi&rdquo;, the company has
              built a strong presence in the domestic market and grown into a
              recognized name internationally.
            </p>
            <p>
              Our operations support thousands of skilled artisans who handcraft
              beedis without the use of chemicals, preserving authenticity and
              craftsmanship that stand the test of time.
            </p>
            <p>
              From its humble beginnings in Mangalore, MGBW has evolved into one
              of India&apos;s leading beedi manufacturers, with products now
              exported to several countries across the globe. Guided by
              innovation, traditional values, and customer trust, Mangalore
              Ganesh Beedi Works is well-positioned for continued growth and
              industry leadership.
            </p>
          </div>
        </div>
      </section>

      {/* History */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">
            History of 501 Mangalore Ganesh Beedi Works
          </h2>
          <div className="text-gray-600 leading-relaxed space-y-4">
            <p>
              Mangalore Ganesh Beedi Works (MGBW), incorporated in 1940, is
              headquartered in Mysuru, India. As one of the oldest and most
              respected beedi manufacturers in the country, MGBW is renowned for
              its commitment to producing high-quality, expertly packed beedis
              crafted from premium tobacco blends.
            </p>
            <p>
              Founded in 1940 by Sri Bantwal Raghuram Prabhu and Sri Madhav
              Shenoi in the peaceful village of Bantwal, South Canara district of
              Karnataka, MGBW has evolved into one of India&apos;s most iconic
              and respected beedi manufacturers.
            </p>
            <p>
              Today, the company is under the capable leadership of Mr. Jagannath
              Shenoi (Managing Partner) and Mr. Govind Shenoy (Executive
              Partner), who equally share responsibilities in driving the
              business forward. MGBW operates multiple strategically located
              manufacturing units across Karnataka, Tamil Nadu, and Telangana.
            </p>
          </div>
        </div>
      </section>

      {/* Manufacturing */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-2">Manufacturing Operations</h2>
          <p className="text-pink-600 mb-8">
            Built for Scale, Designed for Quality
          </p>
          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <h3 className="font-bold text-lg mb-4">Key Capabilities</h3>
              <ul className="space-y-2 text-gray-600">
                <li>• Centralized inventory management</li>
                <li>• Batch-wise tracking &amp; labeling</li>
                <li>• Hygiene-compliant packaging</li>
                <li>• Flexible packaging sizes for global partners</li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-lg mb-4">Product Highlights</h3>
              <ul className="space-y-2 text-gray-600">
                <li>• Rich aroma and consistent burn quality</li>
                <li>• Elegant, traditional packaging</li>
                <li>• 100% all-natural tendu leaves</li>
                <li>• Real tobacco, no substitutes</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Global Reach */}
      <section className="py-20 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Global Reach — Expanding Worldwide
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {globalReach.map((g) => (
              <div key={g.region} className="bg-white rounded-xl p-6 shadow-sm">
                <div className="flex items-center gap-2 mb-3">
                  <h3 className="font-bold text-lg">{g.region}</h3>
                  {g.comingSoon && (
                    <span className="text-xs bg-pink-100 text-pink-600 px-2 py-0.5 rounded-full">
                      Coming Soon
                    </span>
                  )}
                </div>
                <p className="text-gray-600 text-sm">{g.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-8">
            Why Distributors Choose Us
          </h2>
          <div className="grid sm:grid-cols-2 gap-4">
            {whyChooseUs.map((item) => (
              <div
                key={item}
                className="flex items-center gap-3 p-4 bg-gray-50 rounded-lg"
              >
                <span className="text-pink-600 font-bold text-xl">✓</span>
                <span className="text-gray-700">{item}</span>
              </div>
            ))}
          </div>
          <blockquote className="mt-12 border-l-4 border-pink-600 pl-6 italic text-gray-600">
            &ldquo;We&apos;ve been sourcing from MGBW for over 30 years. Their
            consistency, ethics, and product strength make them the best in the
            market.&rdquo;
            <br />
            <span className="not-italic font-semibold text-gray-900">
              — Distributor from North America
            </span>
          </blockquote>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-pink-600 text-white text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">
          Let&apos;s Grow Together
        </h2>
        <p className="mb-6 opacity-90 max-w-xl mx-auto">
          Trusted by millions. Delivered with integrity. Let&apos;s partner to
          take 501 Ganesh Beedi global.
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
