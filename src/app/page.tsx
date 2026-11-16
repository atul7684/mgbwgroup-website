import Image from "next/image";
import Link from "next/link";

const businesses = [
  {
    title: "Mangalore Ganesh Beedi Works",
    description:
      "Established in 1940, Mangalore Ganesh Beedi is a trusted name in India's beedi industry, renowned for its heritage of quality and consistency. Our flagship 501 Ganesh Beedi continues to serve millions, with growing reach across domestic and global markets.",
    href: "/businesses/mangalore-ganesh-beedi",
    image: "/images/business/ganeshbeedi/ganeshbeedi-hero.jpg",
    cta: "Explore More",
  },
  {
    title: "Shukra Beedies LLP",
    description:
      "Incorporated in 1982, Shukra Beedies LLP brings tradition and precision together to deliver consistent quality and trusted craftsmanship. With a strong foundation and a focus on responsible manufacturing, we continue to serve evolving markets with integrity.",
    href: "/businesses/shukra-beedi",
    image: "/images/business/shukrabeedi/shukrabeedi-hero.jpg",
    cta: "Explore More",
  },
  {
    title: "J&G Agarbatti",
    description:
      "Blending natural ingredients with traditional craftsmanship, J&G Agarbatti creates premium incense products that elevate every space. With a commitment to quality and sustainability, we bring fragrance to homes, temples, and hearts across India.",
    href: "/businesses/jg-agarbatthi",
    image: "/images/business/jg/jg-hero.jpg",
    cta: "Explore More",
  },
  {
    title: "Silent Shores Resorts & Spa",
    description:
      "Nestled by a tranquil lake in Mysuru, Silent Shores is a luxury resort offering serene stays, holistic wellness, and curated experiences. Whether for leisure, celebrations, or rejuvenation, it's where calm meets comfort.",
    href: "https://www.silentshores.com",
    image: "/images/homepage/silent-shores.jpg",
    cta: "Explore More",
    external: true,
  },
  {
    title: "MGBW Garage",
    description:
      "Fueled by speed, powered by passion. MGBW Garage dives into the world of high-performance machines, motorsport vibes, and adrenaline-fueled builds. It's not just about cars — it's a lifestyle on wheels.",
    href: "https://www.instagram.com/mgbwgarage",
    image: "/images/homepage/mgbw-garage.jpg",
    cta: "Follow Us",
    external: true,
  },
  {
    title: "501 Safety Matches",
    description:
      "Introduced in August 2025, 501 Safety Matches extend the trusted promise of MGBW Group into a complementary product line. Designed for everyday convenience and reliability, they carry forward the same commitment to quality and consistency that defines all our brands.",
    href: "#",
    image: "/images/homepage/501-matches.jpg",
    cta: "Coming Soon",
  },
];

const timeline = [
  {
    year: "1940",
    title: "Mangalore Ganesh Beedi Works Founded",
    description:
      "The beginning of a trusted enterprise rooted in quality, discipline, and values.",
  },
  {
    year: "1982",
    title: "Shukra Beedies Incorporated",
    description:
      "Expanding operations with a focus on consistency, scale, and reliability in production.",
  },
  {
    year: "2007",
    title: "Launch of Silent Shores",
    description:
      "Venturing into premium hospitality with a lakeside luxury retreat in Mysuru.",
  },
  {
    year: "2018",
    title: "Introduction of J&G Agarbatti",
    description:
      "Bringing natural fragrances and sustainable incense products to homes and temples across India.",
  },
  {
    year: "2023",
    title: "MGBW Garage Gains Digital Momentum",
    description:
      "Stepping into the digital era with an automotive lifestyle brand built for passion.",
  },
  {
    year: "2025",
    title: "501 Safety Matches Launched",
    description:
      "Expanding into everyday essentials with a reliable, complementary product for beedis and agarbattis.",
  },
  {
    year: "2026",
    title: "Shukra Deepam Oil",
    description:
      "Bringing a trusted traditional essential to everyday worship, crafted to support a bright, steady flame for your pooja rituals.",
  },
  {
    year: "Present",
    title: "Growth Across Sectors and Borders",
    description:
      "Continuing to evolve with tradition and vision, touching lives across industries and geographies.",
  },
];

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="relative h-[90vh] flex items-center justify-center bg-gray-900">
        <div className="absolute inset-0">
          <Image
            src="/images/homepage/hero-bg.jpg"
            alt="MGBW Group"
            fill
            className="object-cover opacity-40"
            priority
          />
        </div>
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-5xl md:text-7xl font-bold mb-4">MGBW GROUP</h1>
          <p className="text-xl md:text-2xl font-light tracking-wide">
            THE TRADITION OF TRUST SINCE 1940
          </p>
        </div>
      </section>

      {/* About Intro */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-sm uppercase tracking-widest text-pink-600 mb-4">
            When you choose us, you can expect
          </p>
          <h2 className="text-3xl md:text-4xl font-bold mb-8">The MGBW Group</h2>
          <p className="text-gray-600 leading-relaxed text-lg">
            With over nine decades of history,{" "}
            <span className="font-semibold text-gray-900">MGBW Group</span> is a
            family-driven enterprise built on trust, tradition, and principled
            growth. What began as a modest vision has evolved into a diversified
            organization with a wide-reaching impact across industries and
            generations. Our journey is rooted in a deep commitment to ethical
            business practices, long-term relationships, and meaningful
            contributions to the communities we serve. Guided by the underlying
            principles of our founder, we continue to build with purpose, lead
            with integrity, and create value that stands the test of time.
          </p>
          <Link
            href="/about"
            className="inline-block mt-8 px-8 py-3 bg-pink-600 text-white rounded-full hover:bg-pink-700 transition"
          >
            Discover Our Story
          </Link>
        </div>
      </section>

      {/* Our Businesses */}
      <section className="py-20 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-16">
            Our Businesses
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {businesses.map((biz) => (
              <div
                key={biz.title}
                className="bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition group"
              >
                <div className="relative h-48 overflow-hidden">
                  <Image
                    src={biz.image}
                    alt={biz.title}
                    fill
                    className="object-cover group-hover:scale-105 transition duration-500"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-bold mb-3">{biz.title}</h3>
                  <p className="text-gray-600 text-sm leading-relaxed mb-4">
                    {biz.description}
                  </p>
                  {biz.external ? (
                    <a
                      href={biz.href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-pink-600 font-semibold text-sm hover:underline"
                    >
                      {biz.cta} →
                    </a>
                  ) : (
                    <Link
                      href={biz.href}
                      className="text-pink-600 font-semibold text-sm hover:underline"
                    >
                      {biz.cta} →
                    </Link>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Timeline */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-16">
            A Journey Through Time
          </h2>
          <div className="relative">
            {/* Vertical line */}
            <div className="absolute left-1/2 transform -translate-x-1/2 h-full w-0.5 bg-pink-200" />
            <div className="space-y-12">
              {timeline.map((item, i) => (
                <div
                  key={item.year}
                  className={`flex items-center ${
                    i % 2 === 0 ? "flex-row" : "flex-row-reverse"
                  }`}
                >
                  <div className="w-5/12">
                    <div
                      className={`${
                        i % 2 === 0 ? "text-right pr-8" : "text-left pl-8"
                      }`}
                    >
                      <span className="text-pink-600 font-bold text-lg">
                        {item.year}
                      </span>
                      <h3 className="font-bold text-lg mt-1">{item.title}</h3>
                      <p className="text-gray-600 text-sm mt-2">
                        {item.description}
                      </p>
                    </div>
                  </div>
                  <div className="w-2/12 flex justify-center">
                    <div className="w-4 h-4 bg-pink-600 rounded-full border-4 border-pink-100 z-10" />
                  </div>
                  <div className="w-5/12" />
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 px-4 bg-pink-600 text-white text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-4">
          Have questions or need more information? We&apos;re here to help!
        </h2>
        <Link
          href="/contact"
          className="inline-block mt-4 px-8 py-3 bg-white text-pink-600 rounded-full font-semibold hover:bg-gray-100 transition"
        >
          CONTACT US
        </Link>
      </section>
    </>
  );
}
